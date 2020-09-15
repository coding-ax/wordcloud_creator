import searchPage from '../views/searchPage'
import resPage from '../views/resPage'
export default [
    {
        path: '/',
        exact: true,
        component: searchPage,
    },
    {
        path: '/res/:value',
        exact: true,
        component: resPage,
    }
]