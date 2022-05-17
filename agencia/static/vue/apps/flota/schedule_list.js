new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        schedule_list:[]      
    },
    methods:{
        get_schedule_list: function (){
            var self = this;

            axios.get('/garage/api/schedule/list').then(function (response){
                self.schedule_list = response.data
            })
        }
    },
    beforeMount(){
        this.get_schedule_list()
     },
});