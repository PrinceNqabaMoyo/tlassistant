export const routePathMap = {
  landing: '/',
  privacy: '/privacy',
  signin: '/signin',
  signup: '/signup',
  verifyEmail: '/verify-email',
  subscribe: '/subscribe',
  dashboard: '/dashboard',
  app: '/app',
  sandbox: '/sandbox',
};

export const getRequestedRouteFromPath = (pathname = '/') => {
  const normalizedPath = pathname.replace(/\/+$/, '') || '/';

  if (normalizedPath === '/sandbox') return 'sandbox';
  if (normalizedPath === '/privacy') return 'privacy';
  if (normalizedPath === '/signin') return 'signin';
  if (normalizedPath === '/signup') return 'signup';
  if (normalizedPath === '/verify-email') return 'verifyEmail';
  if (normalizedPath === '/subscribe') return 'subscribe';
  if (normalizedPath === '/test-drive') return 'signup';
  if (normalizedPath === '/dashboard') return 'dashboard';
  if (normalizedPath === '/app') return 'app';
  return 'landing';
};

export const resolveRoutePage = (requestedPage, isAuthenticated, hasVerifiedAccess = false, isAnonymous = false) => {
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
