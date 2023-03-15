<template>
  <div id="app">
    <div class="chat-container">
      <message-list :messages="messages" />
      <chat-input @send-message="addMessage" />
    </div>
  </div>
</template>

<script>
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
  methods: {
    addMessage(content) {
      if (content.trim() === "") return;

      this.messages.push({
        type: "human",
        text: content.trim(),
      });

      this.getBotReply(content);
    },
    getBotReply(content) {
      // 模拟机器人回复
      setTimeout(() => {
        this.messages.push({
          type: "robot",
          text: `You said: "${content}".`, // 这里是模拟回复，您需要替换为实际的 API 调用
        });
      }, 1000);
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
