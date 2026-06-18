export const routePathMap = {
  landing: '/',
  signin: '/signin',
  signup: '/signup',
  verifyEmail: '/verify-email',
  subscribe: '/subscribe',
  dashboard: '/dashboard',
  app: '/app',
};

export const getRequestedRouteFromPath = (pathname = '/') => {
  const normalizedPath = pathname.replace(/\/+$/, '') || '/';

  if (normalizedPath === '/signin') return 'signin';
  if (normalizedPath === '/signup') return 'signup';
  if (normalizedPath === '/verify-email') return 'verifyEmail';
  if (normalizedPath === '/subscribe') return 'subscribe';
  if (normalizedPath === '/dashboard') return 'dashboard';
  if (normalizedPath === '/app') return 'app';
  return 'landing';
};

export const resolveRoutePage = (requestedPage, isAuthenticated, hasVerifiedAccess = false) => {
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
