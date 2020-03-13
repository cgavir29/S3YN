<template>
  <div class="container">
    <b-field>
      <b-select placeholder="Database">
        <option>PostgreSQL</option>
        <option>MySQL</option>
        <option>SQLite</option>
      </b-select>
    </b-field>

    <b-field>
      <b-select placeholder="Table">
        <option>Temperature</option>
        <option>GPS</option>
      </b-select>
    </b-field>

    <b-button class="has-text-weight-bold is-warning">Query</b-button>
  </div>
</template>
