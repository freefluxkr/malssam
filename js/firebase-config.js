// Firebase Configuration for Malssam
const firebaseConfig = {
  apiKey: "AIzaSyBcS8aS5yHk2KFNYPImXslsFkSyoBwYrKI",
  authDomain: "dmdg-live.firebaseapp.com",
  projectId: "dmdg-live",
  storageBucket: "dmdg-live.firebasestorage.app",
  messagingSenderId: "357433220336",
  appId: "1:357433220336:web:1a8914811da09123a0f635",
  measurementId: "G-RRYE7JKKWX"
};

if (typeof firebase !== 'undefined') {
  if (!firebase.apps || !firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
  }
  window.firestoreDb = firebase.firestore();
}