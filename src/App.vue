<template>
  <div id="app">
    <h1>PlantFarm Bot _ Test</h1>
    <div class="chat-box">
      <div v-for="message in chatMessages" :key="message.id" :class="['message', message.type]">
        {{ message.content }}
      </div>
    </div>
    <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Type your message..." />
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInput: '',
      chatMessages: []
    };
  },
  methods: {
    sendMessage() {
  // 사용자가 보낸 메시지가 비어 있는지 확인
  if (!this.userInput.trim()) {
    return; // 빈 메시지인 경우 메시지를 추가하지 않고 종료
  }

  // 사용자가 보낸 메시지 추가
  this.chatMessages.push({
    id: Date.now(),
    content: this.userInput,
    type: 'user'
  });

  // 챗봇 응답 생성 및 추가 (임시로 예시 응답 사용)
  // 챗봇의 응답을 사용자 메시지를 받은 후에 바로 추가
  this.chatMessages.push({
    id: Date.now() + 1,
    content: '안녕하세요. Test 중입니다.',
    type: 'bot'
  });

  // 입력 필드 초기화
  this.userInput = '';
}
  }
};
</script>

<style scoped>
.chat-box {
  height: 300px;
  overflow-y: auto;
}
.message {
  margin: 5px;
  padding: 10px;
  border-radius: 5px;
}
.user {
  background-color: lightblue;
  align-self: flex-start;
}
.bot {
  background-color: lightgreen;
  align-self: flex-end;
}
</style>