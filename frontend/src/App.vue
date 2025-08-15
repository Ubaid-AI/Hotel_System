<script setup>
import { ref, onMounted } from 'vue';

const rooms = ref([]);
const loaded = ref(false);

onMounted(async () => {
  try {
    const res = await fetch('/api/method/havenir_hotel_erpnext.api.rooms.get_available_rooms');
    if (res.ok) {
      const data = await res.json();
      rooms.value = data.message || [];
    }
  } catch (err) {
    console.error('Failed to load rooms', err);
  } finally {
    loaded.value = true;
  }
});
</script>

<template>
  <main>
    <h1>Available Rooms</h1>
    <ul v-if="rooms.length">
      <li v-for="room in rooms" :key="room.name">
        {{ room.room_number }} - {{ room.name }}
      </li>
    </ul>
    <p v-else-if="loaded">No rooms available.</p>
    <p v-else>Loading...</p>
  </main>
</template>

<style>
main {
  font-family: system-ui, sans-serif;
  max-width: 600px;
  margin: 2rem auto;
}
</style>
