// Google Auth
const auth = firebase.auth();

const whenSignedIn = document.getElementById('whenSignedIn');
const whenSignedOut = document.getElementById('whenSignedOut');

const signInBtn = document.getElementById('signInBtn');
const signOutBtn = document.getElementById('signOutBtn');

const userDetails = document.getElementById('userDetails');

const provider = new firebase.auth.GoogleAuthProvider();

// Firestore

const db = firebase.firestore();

const addData = document.getElementById('addData')
const GPS = document.getElementById('GPSSET')

let DATAref;
let unsubscribe;

    if (user) {
        DATAref = db.collection('Data')

        addData.onclick =() => {
            const {serverTimestamp} = firebase.firestore.fieldvalue;

            DATAref.add({
                uid: user.uid,
                name: faker.commerce.productName();
                createdAt: serverTimestamp()
            });

            
        }

        unsubscribe = DATAref
            .where('uid', '==', user.uid)
            .orderBy('createdAt')
            .onSnapshot(querySnapshot) => {

                const items = querySnapshot.docs.map(doc =>) {

                    return `<li${doc.data().name}</li>`
                });
            }











    }