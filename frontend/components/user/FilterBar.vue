<template>
    <div class="hidden lg:form-control fixed right-10 top-[15vh] 2xl:top-[12vh] border-2 rounded-lg border-accent p-5">
        <label class="input input-bordered flex items-center gap-2 w-[15vw] text-xs overflow-x-auto">
            <input type="text" class="" placeholder="Nashville, TN" 
            v-model="filter.location"
            @keyup.enter="emitFilter(filter)"/>
        </label>
        <div class="">
            <label class="label cursor-pointer">
                <input type="checkbox" name="radio-2" class="checkbox checkbox-primary w-3 h-3"
                @click="handleTypeChange('Remote', $event)"
                :checked="isChecked('Remote')"></input>
                <span class="label-text job-text-color text-xs">Remote</span>
            </label>
            <label class="label cursor-pointer">
                <input type="checkbox" name="" class="checkbox checkbox-primary w-3 h-3"
                @click="handleTypeChange('Hybrid', $event)"
                :checked="isChecked('Hybrid')"></input>
                <span class="label-text job-text-color text-xs">Hybrid</span>
            </label>
            <label class="label cursor-pointer">
                <input type="checkbox" name="" class="checkbox checkbox-primary w-3 h-3"
                @click="handleTypeChange('Onsite', $event)"
                :checked="isChecked('Onsite')"></input>
                <span class="label-text job-text-color text-xs">Onsite</span>
            </label>
            <label class="label cursor-pointer">
                <input type="checkbox" name="" class="checkbox checkbox-primary w-3 h-3"
                v-model="filter.contract"></input>
                <span class="label-text job-text-color text-xs">Direct Hire</span>
            </label> 
        </div>
        <div class="pt-2">
            <label class="input input-bordered flex items-center gap-2 text-xs w-[15vw]">
                <input type="text" class="" placeholder="Years of Experience" 
                v-model="filter.yearsNeeded"
                @keyup.enter="emitFilter(filter)"/>
            </label>
        </div>
        <div class="pt-2">
            <label class="input input-bordered flex items-center gap-2 w-[15vw] overflow-x-auto text-xs">
                <input type="text" class="" placeholder="$" 
                v-model="filter.minSalary"
                @keyup.enter="emitFilter(filter)"/>
            </label>
        </div>
        <div class="pt-2">
            <label class="input input-bordered flex items-center gap-2 overflow-x-auto text-xs w-[15vw]">
                <input type="text" class="" placeholder="$$$" 
                v-model="filter.maxSalary"
                @keyup.enter="emitFilter(filter)"/>
            </label>
        </div>
        <div class="pt-2">
            <label class="input input-bordered flex items-center gap-2 w-[15vw] overflow-x-auto text-xs">
                <input type="text" class="" placeholder="Technologies" 
                v-model="filter.techStack"
                @keyup.enter="emitFilter(filter)"/>
            </label>
        </div>
        <span style="font-size: xx-small;" class="pt-1">* Seperate by comma</span>
        <div class="pt-2 flex space-x-2">
            <button class=" btn btn-secondary 2xl:mx-auto lg:w-[30%] 2xl:w-[20%] rounded-md"
            @click="emitFilter('clear')">Clear</button>
            <button class="btn btn-secondary 2xl:mx-auto lg:w-[68%] 2xl:w-[78%] rounded-md"
            @click="emitFilter(filter)">Filter</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, defineEmits } from 'vue';

interface Filter {
    location: string | null,
    type: string[],
    contract: boolean,
    yearsNeeded: number | null,
    minSalary: number | null,
    maxSalary: number | null,
    techStack: string[] | null
}

const filter = ref<Filter>({
    location: null,
    type: [],
    contract: false,
    yearsNeeded: null,
    minSalary: null,
    maxSalary: null,
    techStack: null
});

const emit = defineEmits(['filter']);

const emitFilter = (userFilter: Filter | String) => {
    if (userFilter != null && userFilter != 'clear') {
        console.log('emitted filter: ' + JSON.stringify(userFilter));
        emit('filter', userFilter);
    } else if (userFilter == 'clear') {
        clearFilters();
        emit('filter', null);
    }
    return;
};

const clearFilters = () => {
  filter.value = {
    location: null,
    type: [],
    contract: false,
    yearsNeeded: null,
    minSalary: null,
    maxSalary: null,
    techStack: null,
  };

};

const addType = (type: string) => {
    if (filter.value.type.includes(type)) {
        return;
    } else {
        filter.value.type.push(type);
    }
};

const removeType = (type: string) => {
  filter.value.type = filter.value.type.filter(t => t !== type);
};

const handleTypeChange = (type: string, event: Event) => {
  const target = event.target as HTMLInputElement; // Assert the target as HTMLInputElement
  if (target.checked) {
    addType(type);
  } else {
    removeType(type);
  }
};

const isChecked = (type: string) => {
    return filter.value.type.includes(type);
};

</script>