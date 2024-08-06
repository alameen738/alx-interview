#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// API URL for the specified movie
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const movie = JSON.parse(body);

  // Get the list of character URLs
  const characters = movie.characters;

  // Function to fetch character name by URL
  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  };

  // Fetch all character names asynchronously
  const fetchAllCharacters = async () => {
    for (const url of characters) {
      try {
        const name = await fetchCharacterName(url);
        console.log(name);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  fetchAllCharacters();
});
