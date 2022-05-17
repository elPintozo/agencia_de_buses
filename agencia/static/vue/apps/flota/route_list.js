new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        route_list:[]      
    },
    methods:{
        get_route_list: function (){
            var self = this;

            axios.get('/garage/api/route/list').then(function (response){
                self.route_list = response.data
            })
        }
    },
    beforeMount(){
        this.get_route_list()
     },
});