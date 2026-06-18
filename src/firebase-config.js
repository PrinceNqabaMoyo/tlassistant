// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB1TOAe3SRf9lJRs6R4sjkVBteeXID-Pgg",
  authDomain: "caps-ai-math-assistant-app.firebaseapp.com",
  projectId: "caps-ai-math-assistant-app",
  storageBucket: "caps-ai-math-assistant-app.firebasestorage.app",
  messagingSenderId: "526445100690",
  appId: "1:526445100690:web:add22f0690ebf1d266b04b",
  measurementId: "G-34HG8NYE07"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);