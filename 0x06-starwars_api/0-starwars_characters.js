#!/usr/bin/node
const request = require('request');

const idFilm = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${idFilm}`, async function (error, response, body) {
  if (error) {
    throw error;
  }

  const film = JSON.parse(body);

  if (film !== undefined && Array.isArray(film.characters)) {
    const characters = film.characters;

    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            console.log(JSON.parse(body).name);
            resolve(body);
          }
        });
      });
    }
  }
});
