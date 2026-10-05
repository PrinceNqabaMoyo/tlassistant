/**
 * Navigation History Service — PWA & Android Hardware Back-Button Manager
 * 
 * Intercepts Android hardware back-button presses and gesture navigation (popstate)
 * to provide native-app UX:
 * 1. Closes open modals without exiting the app.
 * 2. Navigates from active subject workspaces back to Today's Desk.
 * 3. Enforces a 2-second double-tap circuit breaker ("Press back again to exit") at root.
 */

class NavigationHistoryService {
  constructor() {
    this.currentTab = 'desk';
    this.activeModal = null;
    this.handlers = {
      onTabChange: null,
      onModalClose: null,
      onShowExitToast: null,
    };
    this.exitPendingUntil = 0;
    this.isInitialized = false;
    this._popstateHandler = this._handlePopState.bind(this);
  }

  init(initialTab = 'desk') {
    if (this.isInitialized || typeof window === 'undefined') return;

    this.currentTab = initialTab;

    // Ensure root state exists in history stack
    try {
      const state = window.history.state;
      if (!state || !state.fundile) {
        window.history.replaceState(
          { fundile: true, screen: initialTab, modal: null, isRoot: true },
          ''
        );
      }
    } catch (e) {
      console.warn('Navigation history init warning:', e);
    }

    window.addEventListener('popstate', this._popstateHandler);
    this.isInitialized = true;
  }

  destroy() {
    if (typeof window !== 'undefined') {
      window.removeEventListener('popstate', this._popstateHandler);
    }
    this.isInitialized = false;
  }

  registerHandlers({ onTabChange, onModalClose, onShowExitToast }) {
    if (onTabChange) this.handlers.onTabChange = onTabChange;
    if (onModalClose) this.handlers.onModalClose = onModalClose;
    if (onShowExitToast) this.handlers.onShowExitToast = onShowExitToast;
  }

  /**
   * Pushes a new screen (tab) to the history stack.
   */
  pushScreen(tabId) {
    if (typeof window === 'undefined') return;
    if (tabId === this.currentTab && !this.activeModal) return;

    this.currentTab = tabId;
    this.activeModal = null;

    try {
      window.history.pushState(
        { fundile: true, screen: tabId, modal: null, isRoot: tabId === 'desk' },
        ''
      );
    } catch (e) {}
  }

  /**
   * Pushes a modal state to the history stack so pressing Back closes the modal.
   */
  pushModal(modalName) {
    if (typeof window === 'undefined') return;
    this.activeModal = modalName;

    try {
      window.history.pushState(
        { fundile: true, screen: this.currentTab, modal: modalName, isRoot: false },
        ''
      );
    } catch (e) {}
  }

  /**
   * Programmatic close of modal without triggering extra back navigation.
   */
  clearModal() {
    this.activeModal = null;
  }

  _handlePopState(event) {
    const now = Date.now();

    // 1. If a modal is currently open, dismiss the modal and remain in the app
    if (this.activeModal) {
      const closingModal = this.activeModal;
      this.activeModal = null;
      if (typeof this.handlers.onModalClose === 'function') {
        this.handlers.onModalClose(closingModal);
      }
      return;
    }

    // 2. If inside a subject workspace, navigate back to Today's Desk
    if (this.currentTab !== 'desk') {
      this.currentTab = 'desk';
      if (typeof this.handlers.onTabChange === 'function') {
        this.handlers.onTabChange('desk');
      }
      // Re-anchor root state so next press triggers the exit toast
      try {
        window.history.replaceState(
          { fundile: true, screen: 'desk', modal: null, isRoot: true },
          ''
        );
      } catch (e) {}
      return;
    }

    // 3. Already on Today's Desk (Root): Check double-tap exit guard
    if (now < this.exitPendingUntil) {
      // Second back press within 2 seconds -> Allow default exit
      this.exitPendingUntil = 0;
      window.history.back();
    } else {
      // First back press -> Show "Press back again to exit" toast and push guard state
      this.exitPendingUntil = now + 2000;
      if (typeof this.handlers.onShowExitToast === 'function') {
        this.handlers.onShowExitToast('Press back again to exit');
      }

      try {
        window.history.pushState(
          { fundile: true, screen: 'desk', modal: null, isRoot: true },
          ''
        );
      } catch (e) {}
    }
  }
}

const navigationHistoryService = new NavigationHistoryService();
export default navigationHistoryService;
