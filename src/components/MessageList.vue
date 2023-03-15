<!-- <template>
    <div class="message-list">
      <div class="message-wrapper" ref="messageWrapper">
        <message v-for="message in messages" :key="message.id" :message="message" />
      </div>
    </div>
  </template>
   -->
   <template>
    <div class="message-list">
      <message
        v-for="(message, index) in messages"
        :key="index"
        :type="message.type"
        :text="message.text"
      />
    </div>
  </template>
  
  <script>
  import Message from "./Message.vue";
  
  export default {
    name: "MessageList",
    components: {
      Message,
    },
    props: {
      messages: Array,
    },
  };
  </script>
  
  <style scoped>
  .message-list {
    overflow-y: auto;
    padding: 1rem;
    max-height: calc(100vh - 80px);
  }
  </style>
  
  