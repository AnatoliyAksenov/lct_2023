import Vue from 'vue'
import Router from 'vue-router'

// Views
import Main from '@/views/MainMonitor'
import SignalLogs from '@/views/SignalLogs'
import ModelLogs from '@/views/ModelLogs'

Vue.use(Router)

const header = 'CIBAA';

const router = new Router({
    routes: [{
        path: '/',
        name: 'MainMonitor',
        component: Main,
        meta:{ title: 'Главный монитор ' + header}
    }, {
        path: '/signallogs',
        name: 'Logs',
        component: SignalLogs,
        meta:{ title: 'История сигналов ' + header}
    },{
        path: '/modellogs',
        name: 'Models',
        component: ModelLogs,
        meta:{ title: 'Статистика по моделям ' + header}
    }]
});

router.beforeEach((to, from, next) => {
    document.title = to.meta.title;
    next();

})

export default router;