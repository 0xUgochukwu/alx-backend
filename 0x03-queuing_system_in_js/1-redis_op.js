import { createClient, print } from 'redis';

const client = createClient();

client.on("error", (error) => {
  console.log("Redis client not connected to the server:", error.toString())
});


client.on("connect", () => {
  console.log("Redis client connected to the server")
});

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

function displayNewSchool(schoolName) {
  client.GET(schoolName, (err, value) => {
    console.log(value);
  });
}
