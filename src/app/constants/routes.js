export const routePathMap = {
  landing: '/za',
  privacy: '/privacy',
  signin: '/signin',
  signup: '/signup',
  verifyEmail: '/verify-email',
  subscribe: '/subscribe',
  dashboard: '/dashboard',
  app: '/app',
  sandbox: '/sandbox',
  skeleton_zw: '/zw',
  skeleton_tz: '/tz',
  skeleton_ke: '/ke',
  skeleton_gh: '/gh',
  skeleton_ng: '/ng',
};

export const getRequestedRouteFromPath = (pathname = '/') => {
  const normalizedPath = pathname.replace(/\/+$/, '') || '/';

  if (normalizedPath === '/sandbox') return 'sandbox';
  if (normalizedPath === '/privacy') return 'privacy';
  if (normalizedPath === '/signin' || normalizedPath === '/za/signin') return 'signin';
  if (normalizedPath === '/signup' || normalizedPath === '/za/signup') return 'signup';
  if (normalizedPath === '/verify-email' || normalizedPath === '/za/verify-email') return 'verifyEmail';
  if (normalizedPath === '/subscribe' || normalizedPath === '/za/subscribe') return 'subscribe';
  if (normalizedPath === '/test-drive' || normalizedPath === '/za/test-drive') return 'signup';
  if (normalizedPath === '/dashboard' || normalizedPath === '/za/dashboard') return 'dashboard';
  if (normalizedPath === '/app' || normalizedPath === '/za/app') return 'app';

  // Skeletons for upcoming regional curricula
  if (normalizedPath === '/zw') return 'skeleton_zw';
  if (normalizedPath === '/tz') return 'skeleton_tz';
  if (normalizedPath === '/ke') return 'skeleton_ke';
  if (normalizedPath === '/gh') return 'skeleton_gh';
  if (normalizedPath === '/ng') return 'skeleton_ng';

  // Root or /za maps to South African landing
  if (normalizedPath === '/' || normalizedPath === '/za') return 'landing';

  return 'landing';
};

export const resolveRoutePage = (requestedPage, isAuthenticated, hasVerifiedAccess = false, isAnonymous = false) => {
  if (typeof requestedPage === 'string' && requestedPage.startsWith('skeleton_')) {
    return requestedPage;
  }

  if (requestedPage === 'sandbox') {
    return 'sandbox';
  }

  if (requestedPage === 'privacy') {
    return 'privacy';
  }

  if (isAnonymous) {
    if (requestedPage === 'signup' || requestedPage === 'subscribe') {
      return requestedPage;
    }
    return 'landing';
  }

  if (isAuthenticated) {
    if (!hasVerifiedAccess) {
      return 'verifyEmail';
    }

    if (requestedPage === 'subscribe') {
      return 'subscribe';
    }

    if (requestedPage === 'dashboard') {
      return 'dashboard';
    }

    return 'dashboard';
  }

  if (requestedPage === 'dashboard' || requestedPage === 'app' || requestedPage === 'verifyEmail') {
    return 'signin';
  }

  return requestedPage;
};
