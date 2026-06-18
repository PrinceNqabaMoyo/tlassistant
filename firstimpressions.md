# First Impressions Refresh Plan

## Objective
Improve the first impression of Fundile before sign up by making the pre-auth experience feel faster, more modern, and more distinctly branded, while still performing well on slow or unreliable networks.

## What I plan to do

### 1. Make the opening splash feel lighter and faster
- Replace the current Netflix-style typed text reveal with a cleaner, shorter intro.
- Introduce a subtle animation where small orange/yellow squares fall into place and build the graduation cap from the bottom upward.
- Keep the animation lightweight by using simple DOM/CSS/SVG motion instead of large media assets.
- Reduce perceived wait time by shortening the total intro duration.
- Avoid repeated expensive network-dependent styling inside the splash artwork.

### 2. Improve startup performance for weak-network situations
- Remove external font imports embedded inside SVG logo components.
- Prefer app-level text styling over SVG-internal font loading.
- Reduce reliance on large background images for the first public-facing screens.
- Keep the first rendered view mostly vector, gradient, and text-based.
- Make sure the splash and landing screen degrade gracefully if fonts or images load slowly.

### 3. Redesign the public landing page into a modern long-scroll page
- Replace the current image-heavy landing page with a cleaner, modern long-scroll layout.
- Use gradients, cards, sections, spacing, and motion rather than large photo backgrounds.
- Add clearer messaging about what Fundile helps students do.
- Add sections such as:
  - Hero section
  - Why Fundile
  - Key workflows/features
  - Who it is for
  - Learning outcomes / value proposition
  - Simple CTA section
- Keep the page visually strong without requiring background photography.

### 4. Improve branding consistency in the browser
- Replace the default Vite tab icon and page title.
- Use a Fundile-branded graduation-cap favicon.
- Update the browser tab title from the Vite default to Fundile branding.
- Update the web app manifest metadata so the Fundile brand also appears correctly where supported.

### 5. Keep the change low-risk
- Limit the first pass to pre-auth branding and public-facing screens.
- Do not touch authenticated student/teacher/admin flows unless required for branding wiring.
- Reuse existing logo assets where safe, and only add small supporting assets if necessary.

## Suggested content direction for the long-scroll landing page
The page should answer these questions quickly:
- What is Fundile?
- Who is it for?
- Why is it better than generic study tools?
- What can a student do in it right away?
- Why should a parent/teacher trust it?

## Candidate content blocks
- Fundile helps South African learners study with more structure and feedback.
- CAPS-aligned support for targeted grade and subject learning.
- Practice, tutoring, assignments, and guided feedback in one place.
- Designed for students who need clarity, repetition, and momentum.
- Built to support both independent study and teacher-guided learning.

## Files I expect to edit in the first implementation pass
- `src/components/ui/SplashScreen.jsx`
- `src/components/ui/GraduationCapSplash.jsx`
- `src/components/ui/LandingPage.jsx`
- `src/components/ui/FundileLogo.jsx`
- `src/hooks/useCoreState.js`
- `src/App.jsx`
- `index.html`
- `public/manifest.json`
- `public/favicon.ico` or replacement favicon asset(s)
- `public/logo192.png` and `public/logo512.png` if app branding icons are refreshed

## Files to back up before any edits
- `src/components/ui/SplashScreen.jsx`
- `src/components/ui/GraduationCapSplash.jsx`
- `src/components/ui/LandingPage.jsx`
- `src/components/ui/FundileLogo.jsx`
- `src/hooks/useCoreState.js`
- `src/App.jsx`
- `index.html`
- `public/favicon.ico`
- `public/manifest.json`
- `public/logo192.png`
- `public/logo512.png`
- `public/vite.svg`

## Notes
- No visual edits have been applied yet in this planning step.
- The current root `index.html` is the active Vite HTML entry and should definitely be backed up.
- The current public landing page is image-heavy and is the main candidate for modernization.
