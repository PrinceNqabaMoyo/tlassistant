import { useCallback, useEffect, useRef, useState } from 'react';
import { getRequestedRouteFromPath, resolveRoutePage, routePathMap } from '../constants/routes';

export const useTopLevelRouting = ({
  authLoading,
  hasVerifiedAccess,
  isAuthenticated,
  setShowLandingPage,
  setShowSplash,
  showSplash,
}) => {
  const [routePage, setRoutePage] = useState(() => {
    if (typeof window === 'undefined') return 'landing';
    return getRequestedRouteFromPath(window.location.pathname);
  });

  const hasResolvedInitialAuthViewRef = useRef(false);
  const hasInitializedBrowserHistoryRef = useRef(false);
  const previousTopLevelPageRef = useRef(null);
  const isHandlingBrowserNavigationRef = useRef(false);

  const topLevelPage = resolveRoutePage(routePage, isAuthenticated, hasVerifiedAccess);
  const shouldRenderStandaloneLandingPage = topLevelPage === 'landing' && (!isAuthenticated || hasResolvedInitialAuthViewRef.current);
  const authMode = topLevelPage === 'signup' ? 'signup' : 'signin';

  useEffect(() => {
    if (authLoading || showSplash) {
      return;
    }

    const resolvedPage = resolveRoutePage(routePage, isAuthenticated, hasVerifiedAccess);

    if (routePage !== resolvedPage) {
      setRoutePage(resolvedPage);
    }

    if (!hasResolvedInitialAuthViewRef.current) {
      hasResolvedInitialAuthViewRef.current = true;
    }
  }, [authLoading, hasVerifiedAccess, showSplash, isAuthenticated, routePage]);

  useEffect(() => {
    setShowLandingPage(topLevelPage === 'landing');
  }, [topLevelPage, setShowLandingPage]);

  const handleSplashComplete = useCallback(() => {
    setShowSplash(false);

    if (!authLoading) {
      setRoutePage((currentRoutePage) => resolveRoutePage(currentRoutePage, isAuthenticated, hasVerifiedAccess));
    }
  }, [authLoading, hasVerifiedAccess, isAuthenticated, setShowSplash]);

  const navigateToRoutePage = useCallback((nextPage) => {
    setRoutePage(nextPage);
  }, []);

  const handleNavigateHome = useCallback(() => {
    navigateToRoutePage('landing');
  }, [navigateToRoutePage]);

  const handleNavigateSignIn = useCallback(() => {
    navigateToRoutePage('signin');
  }, [navigateToRoutePage]);

  const handleNavigateSignUp = useCallback(() => {
    navigateToRoutePage('signup');
  }, [navigateToRoutePage]);

  const handleNavigateToSubscriptionPage = useCallback(() => {
    navigateToRoutePage('subscribe');
  }, [navigateToRoutePage]);

  const handleNavigateToDashboard = useCallback(() => {
    navigateToRoutePage('dashboard');
  }, [navigateToRoutePage]);

  const handleNavigateToApp = useCallback(() => {
    navigateToRoutePage('dashboard');
  }, [navigateToRoutePage]);

  useEffect(() => {
    if (showSplash || typeof window === 'undefined') {
      return;
    }

    const handlePopState = (event) => {
      const requestedPage = event.state?.fundilePage || getRequestedRouteFromPath(window.location.pathname);

      isHandlingBrowserNavigationRef.current = true;
      setRoutePage(resolveRoutePage(requestedPage, isAuthenticated, hasVerifiedAccess));
    };

    window.addEventListener('popstate', handlePopState);

    return () => window.removeEventListener('popstate', handlePopState);
  }, [hasVerifiedAccess, showSplash, isAuthenticated]);

  useEffect(() => {
    if (showSplash || authLoading || typeof window === 'undefined') {
      return;
    }

    const nextPath = routePathMap[topLevelPage] || routePathMap.landing;
    const nextHistoryState = { fundilePage: topLevelPage };

    if (isHandlingBrowserNavigationRef.current) {
      if (window.location.pathname !== nextPath) {
        window.history.replaceState(nextHistoryState, '', nextPath);
      }

      previousTopLevelPageRef.current = topLevelPage;
      isHandlingBrowserNavigationRef.current = false;
      return;
    }

    if (!hasInitializedBrowserHistoryRef.current) {
      window.history.replaceState(nextHistoryState, '', nextPath);
      previousTopLevelPageRef.current = topLevelPage;
      hasInitializedBrowserHistoryRef.current = true;
      return;
    }

    const previousTopLevelPage = previousTopLevelPageRef.current;

    if (previousTopLevelPage === topLevelPage && window.location.pathname === nextPath) {
      return;
    }

    window.history.pushState(nextHistoryState, '', nextPath);

    previousTopLevelPageRef.current = topLevelPage;
  }, [authLoading, showSplash, topLevelPage]);

  const resetTopLevelRouting = useCallback(() => {
    hasResolvedInitialAuthViewRef.current = false;
    hasInitializedBrowserHistoryRef.current = false;
    previousTopLevelPageRef.current = null;
    isHandlingBrowserNavigationRef.current = false;
    setRoutePage('landing');
  }, []);

  return {
    authMode,
    handleNavigateHome,
    handleNavigateSignIn,
    handleNavigateSignUp,
    handleNavigateToDashboard,
    handleNavigateToApp,
    handleNavigateToSubscriptionPage,
    handleSplashComplete,
    navigateToRoutePage,
    resetTopLevelRouting,
    shouldRenderStandaloneLandingPage,
    topLevelPage,
  };
};
