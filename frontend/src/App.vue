<template>
  <div>
    <nav class="navbar">
      <h1>Restaurant Reservations</h1>
      <div class="nav-links">
        <router-link to="/">Reservar</router-link>
        <router-link to="/cancel">Cancelar reserva</router-link>
        <router-link to="/admin-reservations">Admin</router-link>
      </div>
    </nav>

    <main class="container">
      <router-view />
    </main>
  </div>
</template>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f4f4f4;
}

.navbar {
  background: #1f2937;
  color: white;
  padding: 16px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links a {
  color: white;
  text-decoration: none;
  margin-left: 16px;
  font-weight: bold;
}

.container {
  max-width: 900px;
  margin: 30px auto;
  padding: 20px;
}
</style>