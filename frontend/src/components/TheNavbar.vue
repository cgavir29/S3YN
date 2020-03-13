<template>
  <div class="hero-head">
    <header class="navbar">
      <div class="container">
        <div class="navbar-brand">
          <router-link class="navbar-item title has-text-warning" :to="{ name : 'home' }">S3YN</router-link>
          <!-- <span class="navbar-burger burger" data-target="navbarMenuHeroC">
            <span></span>
            <span></span>
            <span></span>
          </span>-->
        </div>
        <div id="navbarMenuHeroC" class="navbar-menu">
          <div class="navbar-end">
            <router-link
              class="navbar-item"
              :to="{ name : 'home' }"
              active-class="is-active"
              exact
            >Home</router-link>
            <router-link
              class="navbar-item"
              :to="{ name : 'about' }"
              active-class="is-active"
              exact
            >About</router-link>

            <span class="navbar-item">
              <a class="button is-success is-inverted">
                <span class="icon">
                  <i class="fas fa-sign-in-alt"></i>
                </span>
                <span>Sign in</span>
              </a>
            </span>
            <span class="navbar-item">
              <a class="button is-success is-inverted">
                <span class="icon">
                  <i class="fas fa-user"></i>
                </span>
                <span>Sign up</span>
              </a>
            </span>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>
