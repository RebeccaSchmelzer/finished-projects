import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyBc3sGBuQsTjHVSzYOrNlH347vB6AQ2dEY",
  authDomain: "becflix-c1110.firebaseapp.com",
  projectId: "becflix-c1110",
  storageBucket: "becflix-c1110.appspot.com",
  messagingSenderId: "118494743000",
  appId: "1:118494743000:web:e2d4842cd8dc316c890aad"
};

const firebaseapp = firebase.initializeApp(firebaseConfig);
const db = firebaseapp.firestore();
const auth = firebase.auth();

export { auth, db };