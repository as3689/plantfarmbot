<template>
    <div>
      <input v-model="userInput" @keyup.enter="sendMessage" type="text" placeholder="Type a message..." />
      <div v-for="(message, index) in messages" :key="index">
        {{ message }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userInput: '',
        messages: []
      };
    },
    methods: {
      sendMessage() {
        this.messages.push("You: " + this.userInput);
        fetch('http://127.0.0.1:5000/api/chatbot', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            message: this.userInput
          })
        })
        .then(response => response.json())
        .then(data => {
          this.messages.push("Bot: " + data.response);
          this.userInput = '';
        });
      }
    }
  };
  </script>
  
  <style scoped>
  /* 스타일을 여기에 추가하세요 */
  </style>
  