
<!-- <template>
  <div id="app">
    <message-list class="message-list" :messages="messages" />
    <chat-input @send-message="addMessage" />
  </div>
</template> -->
<template>
  <div id="app">
    <div class="chat-container">
      <message-list :messages="messages" />
      <div class="input-box">
        <input v-model="inputText" @keyup.enter="sendMessage" type="text" placeholder="Type your message..." />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>


<!-- <script>
import { ref } from 'vue';
import axios from 'axios';
import ChatInput from './components/ChatInput.vue';
import MessageList from './components/MessageList.vue';

export default {
  components: {
    ChatInput,
    MessageList
  },
  setup() {
    const messages = ref([]);

    async function addMessage(content) {
      const message = { content, isBot: false };
      messages.value.push(message);

      // 调用你的 Python 脚本 API，用以下 URL 替换示例 URL
      const apiUrl = 'https://example.com/your-chatbot-api';
      try {
        const response = await axios.post(apiUrl, { message: content });
        const botMessage = {
          content: response.data.reply,
          isBot: true
        };
        messages.value.push(botMessage);
      } catch (error) {
        console.error('Failed to fetch chatbot response:', error);
      }
    }

    return {
      messages,
      addMessage
    };
  }
};
</script> -->
<script>
import MessageList from "./components/MessageList.vue";

export default {
  name: "App",
  components: {
    MessageList,
  },
  data() {
    return {
      inputText: "",
      messages: [
        {
          type: "robot",
          text: "Hi, I'm your chatbot! How can I help you?",
        },
      ],
    };
  },
  methods: {
    sendMessage() {
      if (this.inputText.trim() === "") return;

      this.messages.push({
        type: "human",
        text: this.inputText.trim(),
      });

      this.inputText = "";
    },
  },
};
</script>



<style>
body {
  margin: 0;
  font-family: 'Roboto', sans-serif;
  background-color: #1a1a1a;
}
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%; /* 设置宽度为100%，使其覆盖整个屏幕 */
}
.chat-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
  padding-bottom: 80px;
}

.input-box {
  display: flex;
  align-items: center;
  background-color: #2c2c2c;
  padding: 1rem;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
}

.input-box input {
  flex-grow: 1;
  padding: 0.5rem;
  margin-right: 1rem;
  border: none;
  border-radius: 5px;
  outline: none;
}

.input-box button {
  background-color: #4b7bec;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.input-box button:hover {
  background-color: #3f6edc;
}
</style>
