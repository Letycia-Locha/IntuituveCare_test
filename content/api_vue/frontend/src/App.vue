<script setup>
import { ref } from 'vue'

const busca = ref('')

const abrirNovaAba = () => {
  if (busca.value.length >= 3) {
    const url = `http://127.0.0.1:5000/buscar-operadora?query=${encodeURIComponent(busca.value)}`
    window.open(url, '_blank')
  } else {
    alert("Digite pelo menos 3 letras para pesquisar.")
  }
}
</script>

<template>
  <div class="container">
    <h1>Busca de Operadoras</h1>

    <div class="busca-container">
      <input
        v-model="busca"
        type="text"
        placeholder="Digite o nome da operadora"
      />
      <button @click="abrirNovaAba">Pesquisar</button>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 2rem auto;
  font-family: sans-serif;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.95);
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

p {
  color: black;
  font-weight: 500;
  margin-top: 1rem;
}

h1 {
  color: #4B0082; /* roxo escuro */
  font-weight: 400;
  margin-bottom: 1rem;
}

.busca-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}

input {
  width: 100%;
  max-width: 350px;
  padding: 0.75rem;
  border: 2px solid #B57EDC; /* contorno lilás */
  border-radius: 12px;
  font-size: 1rem;
  background-color: white;
  color: black;
  outline: none;
  text-align: center;
}

button {
  padding: 0.75rem 1.2rem;
  background-color: #6A0DAD; /* roxo */
  color: white;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #4B0082; /* roxo escuro no hover */
}

ul {
  list-style: none;
  padding: 0;
}

li {
  background: #f3f3f3;
  margin: 0.5rem 0;
  padding: 0.75rem;
  border-radius: 6px;
}
</style>
