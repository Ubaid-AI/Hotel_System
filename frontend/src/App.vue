<script setup>
import { ref, onMounted } from 'vue';

const rooms = ref([]);

onMounted(async () => {
  try {
    const res = await fetch('/api/method/havenir_hotel_erpnext.api.rooms.get_available_rooms');
    if (res.ok) {
      const data = await res.json();
      rooms.value = data.message || [];
    }
  } catch (err) {
    console.error('Failed to load rooms', err);
  }
});
</script>

<template>
  <main>
    <h1>Available Rooms</h1>

      <li v-for="room in rooms" :key="room.name">
        {{ room.room_number }} - {{ room.name }}
      </li>
    </ul>
  </main>
</template>

<style>
main {
  font-family: system-ui, sans-serif;
  max-width: 600px;
  margin: 2rem auto;
}
</style>
