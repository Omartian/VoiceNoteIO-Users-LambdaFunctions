const axios = require("axios");
const URL = "http://voicenoteusers-env-1.eba-bhcncxry.us-east-1.elasticbeanstalk.com/"

function randomString(len) {
  var str = "";                                // String result
  for (var i = 0; i < len; i++) {              // Loop len times
    var rand = Math.floor(Math.random() * 62); // random: 0..61
    var charCode = rand += rand > 9 ? (rand < 36 ? 55 : 61) : 48; // Get correct charCode
    str += String.fromCharCode(charCode);      // add Character to str
  }
  return str; // After all loops are done, return the concatenated string
}

function ValidateEmail(email) {
  if (/^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:.[a-zA-Z0-9-]+)$/.test(email))
    return true
  else
    return false
}

exports.handler = async event => {
  const { name, email, password } = event;

  if(ValidateEmail(email) && name.length > 0 && password.length > 5) {
    const request = await axios.request({
      method: 'POST',
      url: URL + 'users/new',
      headers: {
        'Content-Type': 'application/json'
      },
      data: {
        id: randomString(15),
        name,
        email,
        password
      }
    });
    const data = request.data;
    return {
      id: data.user.id,
      name: data.user.name,
      email: data.user.email,
      audios: data.user.audios,
      token: data.token
    }
  } else {
    return {
      errorReason: "Invalid values for email, name and/or password"
    }
  }
};