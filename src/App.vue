

<template>
  <div id="app">
    <div class="chat-container">
      <message-list :messages="messages" />
      <chat-input @send-message="addMessage" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ChatInput from "./components/ChatInput.vue";
import MessageList from "./components/MessageList.vue";

export default {
  name: "App",
  components: {
    ChatInput,
    MessageList,
  },
  data() {
    return {
      messages: [
        {
          type: "robot",
          text: "Hi, I'm your chatbot! How can I help you?",
        },
      ],
    };
  },
  mounted(){
    this.resetBackendData();
  },
  methods: {
    addMessage(content) {
      if (content.trim() === "") return;

      this.messages.push({
        type: "human",
        text: content.trim(),
      });

      this.getBotReply(content);
    },
    async getBotReply(content) {
      const apiUrl = "http://localhost:5000/chatbot";
        try {
          const response = await axios.post(apiUrl, { message: content });
          const botReply = response.data.reply;
          this.messages.push({
            type: "robot",
            text: botReply,
          });
        } catch (error) {
          console.error("Failed to fetch chatbot response:", error);
        }
    },
    async resetBackendData(){
      try{
        await axios.post('http://localhost:5000/reset');
      }catch(error){
        console.error('Failed to reset backend data:',error)
      }
    },
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: "Roboto", sans-serif;
  background-color: #1a1a1a;
}
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
}
.chat-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
  padding-bottom: 80px;
}
</style>
