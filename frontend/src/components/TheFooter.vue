<template>
  <!-- Hero footer: will stick at the bottom -->
  <div class="hero-foot">
    <nav class="tabs is-boxed is-fullwidth">
      <div class="container">
        <ul>
          <router-link tag="li" :to="{ name : 'Databases' }" active-class="is-active" exact>
            <a>Databases</a>
          </router-link>
          <router-link tag="li" :to="{ name : 'Queries' }" active-class="is-active" exact>
            <a>Queries</a>
          </router-link>
          <router-link tag="li" :to="{ name : 'Visualizations' }" active-class="is-active" exact>
            <a>Visualizations</a>
          </router-link>
        </ul>
      </div>
    </nav>
  </div>
</template>
