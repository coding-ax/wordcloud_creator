import searchPage from '../views/searchPage'
import resPage from '../views/resPage'
import frontPage from '../views/frontPage'
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
    },
    {
        path: '/front/:value',
        exact: true,
        component: frontPage
    }
]