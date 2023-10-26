import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	currentInventory: [],
};

const getters = {
	currentInventory: (state) => state.currentInventory,
};

const actions = {

	fetchAllData: ({ commit }) => {
		const path = 'http://localhost:5000/fetchDatabaseData';
		axios.post(path)
			.then((res) => {
				console.log(res.data)
				commit('setCurrentInventory', res.data);
			})
			.catch((error) => {
				console.log(error);
			});
	}, 

	submitDaySalesToDataBase: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/submitSalesDataToDatabase';
		axios.post(path, payload)
			.then((res) => {
				commit('current_inventory', false);
			})
			.catch((error) => {
				console.log(error);
			});
	},


};

const mutations = {

	setCurrentInventory(state, value) {
		state.currentInventory = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};