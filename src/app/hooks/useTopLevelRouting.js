import { useCallback, useEffect, useRef, useState } from 'react';
import { getRequestedRouteFromPath, resolveRoutePage, routePathMap } from '../constants/routes';
import { isStandaloneApp } from '../../hooks/useCoreState';

export const useTopLevelRouting = ({
  authLoading,
  hasVerifiedAccess,
  isAuthenticated,
  setShowLandingPage,
  setShowSplash,
  showSplash,
  isAnonymous,
}) => {
  const [routePage, setRoutePage] = useState(() => {
    if (typeof window === 'undefined') return 'landing';
    const req = getRequestedRouteFromPath(window.location.pathname);
    if (isStandaloneApp() && req === 'landing') {
      return isAuthenticated ? 'dashboard' : 'signin';
    }
    return req;
  });

  const hasResolvedInitialAuthViewRef = useRef(false);
  const hasInitializedBrowserHistoryRef = useRef(false);
  const previousTopLevelPageRef = useRef(null);
  const isHandlingBrowserNavigationRef = useRef(false);

  const topLevelPage = resolveRoutePage(routePage, isAuthenticated, hasVerifiedAccess, isAnonymous);
  const isStandalone = isStandaloneApp();
  const shouldRenderStandaloneLandingPage = !isStandalone && topLevelPage === 'landing' && (!isAuthenticated || hasResolvedInitialAuthViewRef.current);
  const authMode = topLevelPage === 'signup' ? 'signup' : 'signin';

  useEffect(() => {
    if (authLoading || showSplash) {
      return;
    }

    let resolvedPage = resolveRoutePage(routePage, isAuthenticated, hasVerifiedAccess, isAnonymous);
    if (isStandaloneApp() && resolvedPage === 'landing') {
      resolvedPage = isAuthenticated ? 'dashboard' : 'signin';
    }

    if (routePage !== resolvedPage) {
      setRoutePage(resolvedPage);
    }

    if (!hasResolvedInitialAuthViewRef.current) {
      hasResolvedInitialAuthViewRef.current = true;
    }
  }, [authLoading, hasVerifiedAccess, showSplash, isAuthenticated, routePage, isAnonymous]);

  useEffect(() => {
    setShowLandingPage(!isStandalone && topLevelPage === 'landing');
  }, [topLevelPage, setShowLandingPage, isStandalone]);

  const handleSplashComplete = useCallback(() => {
    setShowSplash(false);

    if (!authLoading) {
      setRoutePage((currentRoutePage) => {
        if (isStandaloneApp() && currentRoutePage === 'landing') {
          return isAuthenticated ? 'dashboard' : 'signin';
        }
        return resolveRoutePage(currentRoutePage, isAuthenticated, hasVerifiedAccess, isAnonymous);
      });
    }
  }, [authLoading, hasVerifiedAccess, isAuthenticated, setShowSplash, isAnonymous]);

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
      setRoutePage(resolveRoutePage(requestedPage, isAuthenticated, hasVerifiedAccess, isAnonymous));
    };

    window.addEventListener('popstate', handlePopState);

    return () => window.removeEventListener('popstate', handlePopState);
  }, [hasVerifiedAccess, showSplash, isAuthenticated, isAnonymous]);

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
