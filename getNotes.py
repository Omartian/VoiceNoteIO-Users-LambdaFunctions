const axios = require("axios");
const URL = "http://voicenoteusers-env-1.eba-bhcncxry.us-east-1.elasticbeanstalk.com/"

exports.handler = async event => {
  const { userId } = event;

  if(userId) {
    const request = await axios.request({
      method: 'POST',
      url: URL + 'notes/userid',
      headers: {
        'Content-Type': 'application/json'
      },
      data: {
        userId
      }
    });
    const data = request.data;
    if (!data.msg) {
      return data
    } else {
      return {
        errorReason: data.msg
      }
    }
  } else {
    return {
      errorReason: "Missing userId"
    }
  }
};