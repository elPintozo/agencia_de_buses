new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        data_tab_1: []
    },
    methods:{   
        get_data_tab_1: function (){
            var self = this;
            axios.get('/box_office/ticket/statistics/average').then(function (response){
                self.data_tab_1 = response.data
            })
        },
    },
    beforeMount(){
        this.get_data_tab_1()
    },
});