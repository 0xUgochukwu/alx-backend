import { promisify } from 'util';
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

async function displayNewSchool(schoolName) {
  const GET = promisify(client.GET).bind(client);

  try {
    const value = await GET(schoolName);
    console.log(value);
  } catch (err) {
    console.log(err.toString());
  }
}
