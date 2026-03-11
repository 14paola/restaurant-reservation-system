<template>
  <div class="card">
    <h2>Reserva creada con éxito</h2>
    <p><strong>Código de reserva:</strong> {{ $route.query.code }}</p>
    <p><strong>Mesa asignada:</strong> {{ $route.query.table }}</p>
    <p><strong>Estado:</strong> {{ $route.query.status }}</p>

    <router-link to="/">Crear otra reserva</router-link>
  </div>
</template>

<style scoped>
.card {
  background: white;
  padding: 24px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,.08);
}
</style>