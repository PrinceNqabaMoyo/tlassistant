/**
 * Image compression utilities for geometry diagrams
 * Provides functions to compress base64 images and optimize file sizes
 */

/**
 * Compress a base64 image by reducing quality and/or dimensions
 * @param {string} base64Data - Base64 encoded image data
 * @param {number} quality - Compression quality (0.1 to 1.0)
 * @param {number} maxWidth - Maximum width for resizing
 * @param {number} maxHeight - Maximum height for resizing
 * @returns {Promise<string>} Compressed base64 data
 */
export const compressImage = async (base64Data, quality = 0.8, maxWidth = 800, maxHeight = 600) => {
    return new Promise((resolve, reject) => {
        try {
            // Create image element
            const img = new Image();
            img.onload = () => {
                // Create canvas for compression
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');

                // Calculate new dimensions maintaining aspect ratio
                let { width, height } = img;
                if (width > maxWidth || height > maxHeight) {
                    const ratio = Math.min(maxWidth / width, maxHeight / height);
                    width *= ratio;
                    height *= ratio;
                }

                // Set canvas dimensions
                canvas.width = width;
                canvas.height = height;

                // Draw and compress
                ctx.drawImage(img, 0, 0, width, height);
                const compressedData = canvas.toDataURL('image/jpeg', quality);
                
                resolve(compressedData);
            };

            img.onerror = () => {
                reject(new Error('Failed to load image for compression'));
            };

            img.src = base64Data;
        } catch (error) {
            reject(error);
        }
    });
};

/**
 * Get image size information from base64 data
 * @param {string} base64Data - Base64 encoded image data
 * @returns {Promise<{width: number, height: number, size: number}>}
 */
export const getImageInfo = (base64Data) => {
    return new Promise((resolve, reject) => {
        try {
            const img = new Image();
            img.onload = () => {
                const size = Math.round((base64Data.length * 3) / 4); // Approximate byte size
                resolve({
                    width: img.width,
                    height: img.height,
                    size: size
                });
            };
            img.onerror = () => {
                reject(new Error('Failed to load image'));
            };
            img.src = base64Data;
        } catch (error) {
            reject(error);
        }
    });
};

/**
 * Optimize image based on size and dimensions
 * @param {string} base64Data - Base64 encoded image data
 * @param {number} maxSizeKB - Maximum size in KB
 * @returns {Promise<string>} Optimized base64 data
 */
export const optimizeImage = async (base64Data, maxSizeKB = 100) => {
    try {
        const info = await getImageInfo(base64Data);
        const currentSizeKB = info.size / 1024;

        // If already small enough, return as is
        if (currentSizeKB <= maxSizeKB) {
            return base64Data;
        }

        // Calculate compression ratio needed
        const compressionRatio = maxSizeKB / currentSizeKB;
        const quality = Math.max(0.1, Math.min(1.0, compressionRatio));

        // Calculate new dimensions
        const dimensionRatio = Math.sqrt(compressionRatio);
        const newWidth = Math.round(info.width * dimensionRatio);
        const newHeight = Math.round(info.height * dimensionRatio);

        return await compressImage(base64Data, quality, newWidth, newHeight);
    } catch (error) {
        console.warn('Image optimization failed:', error);
        return base64Data; // Return original if optimization fails
    }
};

/**
 * Batch compress multiple images
 * @param {Array<{id: string, data: string}>} images - Array of image objects
 * @param {number} quality - Compression quality
 * @returns {Promise<Array<{id: string, data: string, originalSize: number, compressedSize: number}>>}
 */
export const batchCompressImages = async (images, quality = 0.8) => {
    const results = [];
    
    for (const image of images) {
        try {
            const originalInfo = await getImageInfo(image.data);
            const compressedData = await compressImage(image.data, quality);
            const compressedInfo = await getImageInfo(compressedData);
            
            results.push({
                id: image.id,
                data: compressedData,
                originalSize: originalInfo.size,
                compressedSize: compressedInfo.size,
                compressionRatio: compressedInfo.size / originalInfo.size
            });
        } catch (error) {
            console.warn(`Failed to compress image ${image.id}:`, error);
            results.push({
                id: image.id,
                data: image.data,
                originalSize: 0,
                compressedSize: 0,
                compressionRatio: 1
            });
        }
    }
    
    return results;
};
