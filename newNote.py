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
  const { userId, title, text } = event;

  if(title.length > 0 && text.length > 0 ) {
    const request = await axios.request({
      method: 'POST',
      url: URL + 'notes/new',
      headers: {
        'Content-Type': 'application/json'
      },
      data: {
        id: randomString(6),
        userId,
        title,
        text
      }
    });
    const data = request.data;
    return data
  } else {
    return {
      errorReason: "Invalid values for title and/or text content"
    }
  }
};