import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	currentInventory: [],
	uniqueGoods: [],
};

const getters = {
	currentInventory: (state) => state.currentInventory,
	uniqueGoods: (state) => state.uniqueGoods,
};

const actions = {

	fetchAllData: ({ commit }) => {
		const path = 'http://localhost:5000/fetchDatabaseData';
		axios.post(path)
			.then((res) => {
				commit('setCurrentInventory', res.data[0]);
				commit('setUniqueGoods', res.data[1])
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

	setUniqueGoods(state, value) {
		state.uniqueGoods = value;
	}

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};