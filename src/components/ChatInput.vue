<template>
    <div class="input-wrapper">
      <input
        v-model="message"
        type="text"
        placeholder="请输入消息"
        @keyup.enter="sendMessage"
        class="message-input"
      />
      <button @click="sendMessage" class="send-button">
        发送
      </button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        message: '',
        buttonStyle: {
          backgroundColor: '#3B82F6'
        }
      };
    },
    methods: {
      sendMessage() {
        if (this.message.trim()) {
          this.$emit('send-message', this.message.trim());
          this.message = '';
        }
      },
      onMouseOver() {
        this.buttonStyle.backgroundColor = '#2563EB';
      },
      onMouseLeave() {
        this.buttonStyle.backgroundColor = '#3B82F6';
      }
    }
  };
  </script>
  
  <style scoped>
  .input-wrapper {
    display: flex;
    align-items: center;
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 1rem;
    background-color: #2d3748; /* 更改输入框背景颜色与主背景相同 */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .message-input {
    flex-grow: 1;
    margin-right: 10px;
    padding: 0.5rem 1rem;
    border: 1px solid #cbd5e0;
    border-radius: 4px;
    outline: none;
    background-color: #4a5568; /* 更改输入框背景颜色 */
    color: #f7fafc;

  }
  
  .send-button {
    padding: 0.5rem 1rem;
    background-color: #4299e1;
    color: white;
    border-radius: 4px;
    font-weight: 600;
    transition: background-color 0.3s ease-in-out;
  }
  
  .send-button:hover {
    background-color: #3182ce;
  }
  </style>