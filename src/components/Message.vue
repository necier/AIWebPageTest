<template>
    <div class="message" :class="type">
      <div class="text">{{ text }}</div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Message",
    props: {
      type: String, // 类型：'human' 或 'robot'
      text: String, // 消息文本
    },
  };
  </script>
  

<style scoped>
.message {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-bottom: 1rem;
  padding: 0.8rem 1.2rem;
  position: relative;
  font-size: 1rem;
  line-height: 1.4;
  max-width: 70%;
  word-wrap: break-word;
}

.message.human {
  align-self: flex-end;
  background-color: #4b7bec;
  color: white;
  border-radius: 20px 0px 20px 20px;
  margin-left: auto;
}

.message.robot {
  align-self: flex-start;
  background-color: #f0f0f0;
  color: #333;
  border-radius: 0px 20px 20px 20px;
  margin-right: auto;
}
</style>







  