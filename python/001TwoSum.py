# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    place_holder_hash = {}
    nums.each_with_index do |num, index|
        place_holder_hash[num] = index 
    end
    nums.each_with_index do |num, index|
        if place_holder_hash[target - nums[index]] != index && place_holder_hash[target - nums[index]] 
            return [(index+1), ((place_holder_hash[target - nums[index]])+1)]
        end
    end
end