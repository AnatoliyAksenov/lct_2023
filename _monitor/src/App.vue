<template>
  <div class="page-container">

      <md-toolbar class="md-primary">
        <md-button class="md-icon-button" @click="sn = true">
          <md-icon>menu</md-icon>
        </md-button>
        <span class="md-title">Exhauster's health monitor</span>

        <div class="md-toolbar-section-end">
          <md-button>{{ user.name}}</md-button>
          <md-button @click="console.log('test')">
            <md-icon>logout</md-icon>
            Выход</md-button>
        </div>
      </md-toolbar>

      <md-drawer :md-active.sync="sn" md-swipeable style="width: 350px">
        <md-toolbar class="md-transparent" md-elevation="0">
          <span class="md-title">Exhauster's health monitor</span>
        </md-toolbar>

        <md-list>
          <md-list-item>
            <md-icon>settings</md-icon>
            <a class="md-list-item-text" href="/#/" @click="sn = false">Главный монитор</a>
          </md-list-item>
          <md-list-item>
            <md-icon>description</md-icon>
            <a class="md-list-item-text" href="/#/signallogs" @click="sn = false">История сигналов</a>
          </md-list-item>
          <md-list-item>
            <md-icon>search</md-icon>
            <a class="md-list-item-text" href="/#/modellogs" @click="sn = false">Статистика по моделям</a>
          </md-list-item>

        </md-list>
      </md-drawer>
      
      <md-content>
        <router-view />
      </md-content>



  </div>
</template>


<script>


export default {
  components: { },
  name: 'App', 
  data: () => ({
      sn: false,
      user: { name: "operator" }
  }),
  created(){

  }
}
</script>

<style scoped>
  .centered-container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  height: 100vh;
  }

  .centered-container .title {
    text-align: center;
    margin-bottom: 30px;
  }

  .centered-container .title img {
      margin-bottom: 16px;
      max-width: 80px;
  }
  
  .centered-container .title .actions {
    pass: 1;
  }

  .centered-container .title .actions .md-button {
    margin: 0;
  }
  
  .centered-container .form {
    margin-bottom: 60px;
  }

  .centered-container .background {
    /*background: url('/static/X.png');*/
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    z-index: 0;
    background-size: 700px;
    background-repeat: no-repeat;
    background-position: center;
  }
  .centered-container .md-content {
    z-index: 1;
    padding: 40px;
    width: 100%;
    max-width: 400px;
    position: relative;
  }
  .centered-container .loading-overlay {
    z-index: 10;
    top: 0;
    left: 0;
    right: 0;
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.9);
    display: flex;
    align-items: center;
    justify-content: center;
  }

</style>

