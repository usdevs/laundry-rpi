const admin = require('firebase-admin');

var serviceAccount = require('/home/pi/hnr/my-awesome-project-9a50a-firebase-adminsdk-l7ym1-53abc2353b.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});


var db = admin.firestore();

var docRef = db.collection('users').doc('alovelace');

var setAda = docRef.set({
  first: 'Ada',
  last: 'Lovelace',
  born: 1815
});

var aTuringRef = db.collection('users').doc('aturing');

var setAlan = aTuringRef.set({
  'first': 'Alan',
  'middle': 'Mathison',
  'last': 'Turing',
  'born': 1912
});

aTuringRef.update({
	age: 'dead'
})

db.collection('users').get()
  .then((snapshot) => {
    snapshot.forEach((doc) => {
      console.log(doc.id, '=>', doc.data());
    });
  })
  .catch((err) => {
    console.log('Error getting documents', err);
  });
