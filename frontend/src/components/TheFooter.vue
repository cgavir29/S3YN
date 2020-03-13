<template>
  <!-- Hero footer: will stick at the bottom -->
  <div class="hero-foot">
    <nav class="tabs is-boxed is-fullwidth">
      <div class="container">
        <ul>
          <router-link tag="li" :to="{ name : 'home' }" active-class="is-active" exact>
            <a>Databases</a>
          </router-link>
          <router-link tag="li" :to="{ name : 'query' }" active-class="is-active" exact>
            <a>Query</a>
          </router-link>
          <router-link tag="li" :to="{ name : 'visualization' }" active-class="is-active" exact>
            <a>Visualization</a>
          </router-link>
        </ul>
      </div>
    </nav>
  </div>
</template>
