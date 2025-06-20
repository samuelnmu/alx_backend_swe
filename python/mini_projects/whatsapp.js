const axios = require("axios");
const { token } = require("./config");

async function sendWhatsappMessage() {
  if (!token) {
    console.error("❌ API token missing. Please check your .env file.");
    return;
  }

  try {
    const response = await axios.post(
      "https://api.apiwap.com/api/v1/whatsapp/send-message",
      {
        phoneNumber: "+254713625483",
        message: "Wozaaaa Samuel",
        type: "text",
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      }
    );

    console.log("✅ Message sent:", response.data);
  } catch (error) {
    console.error(
      "❌ Error sending message:",
      error.response?.data || error.message
    );
  }
}

sendWhatsappMessage();
