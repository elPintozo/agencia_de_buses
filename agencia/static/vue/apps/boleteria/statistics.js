new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        data_tab_1: [],
        select_route: [],
        select: '',
        percentage: '',
        percentage_list: []
    },
    methods:{   
        get_data_tab_1: function (){
            var self = this;
            axios.get('/box_office/ticket/statistics/average').then(function (response){
                self.data_tab_1 = response.data
            })
        },
        btn_buscar_buses: function (){
            var self = this
            var data = {
                'selected_route': self.select,
                'percentage': self.percentage
            }
            axios.post('/box_office/ticket/statistics/percentage', data).then(function (response){
                self.percentage_list = response.data
            })
            
        },
        get_routes_for_select: function (){
            var self = this
            axios.get('/garage/api/route/list').then(function (response){
                self.select_route = response.data
            })
            
        },
    },
    beforeMount(){
        this.get_data_tab_1()
        this.get_routes_for_select()
    },
});