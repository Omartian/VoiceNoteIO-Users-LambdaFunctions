const axios = require("axios");
const URL = "http://voicenoteusers-env-1.eba-bhcncxry.us-east-1.elasticbeanstalk.com/"

exports.handler = async event => {
  const { email, password } = event;

  if(email && password) {
    const request = await axios.request({
      method: 'POST',
      url: URL + 'users/userByEmail',
      headers: {
        'Content-Type': 'application/json'
      },
      data: {
        email,
        password
      }
    });
    const data = request.data;
    if (!data.msg) {
      return {
        id: data.user.id,
        name: data.user.name,
        email: data.user.email,
        audios: data.user.audios,
        token: data.token
      }
    } else {
      return {
        errorReason: data.msg
      }
    }
  } else {
    return {
      errorReason: "Missing email and / or password"
    }
  }
};