clear all
close all

file_path = 'p081_matrix.txt';

% Sample Matrix
% A = [[131, 673, 234, 103, 18];
%     [201, 96, 342, 965, 150];
%     [630, 803, 746, 422, 111];
%     [537, 699, 497, 121, 956];
%     [805, 732, 524, 37, 331]];

A = readmatrix(file_path);



%% Simple approach
% row_ind = size(A, 1);
% col_ind = size(A, 2);
% 
% row_track = [row_ind];
% col_track = [col_ind];
% 
% while (row_ind > 1) | (col_ind > 1)
%     
%     if (row_ind > 1) & (col_ind > 1)
%         left_val = A(row_ind, col_ind - 1);
%         up_val = A(row_ind - 1, col_ind);
% 
%         if left_val == up_val
%             error('Shit')
%             disp('SHit')
%             break
%         end
% 
%         if left_val < up_val
%             col_ind = col_ind - 1;
%         else
%             row_ind = row_ind - 1;
%         end
% 
%         row_track = [row_track row_ind];
%         col_track = [col_track col_ind];
%         
%     elseif row_ind == 1
%         col_ind = col_ind - 1;
%         row_track = [row_track row_ind];
%         col_track = [col_track col_ind];
%         
%     elseif col_ind == 1
%         row_ind = row_ind - 1;
%         row_track = [row_track row_ind];
%         col_track = [col_track col_ind];
%         
%     end
%     
% end
% 
% figure()
% plot(col_track, row_track)
% 
% run_sum = 0;
% for indx = 1:length(row_track)
%     delta = A(row_track(indx), col_track(indx));
%     run_sum = run_sum + delta;
% end
% 
% disp(run_sum)

%% Let's implement Dijkstra's Algorithm
%{
See Here: 

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
%}

unvisited_set = ones(size(A));
tentative_dist = inf(size(A));
tentative_dist(1, 1) = 0;
current_node = zeros(size(A));
current_node(1, 1) = 1;
target_row = size(A, 1);
target_col = size(A, 2);

[row, col] = find(current_node == 1);

% Find the current node
while true
    
    current_dist = tentative_dist(row, col);
    
    % Consider unvisited neighbors
    try
        dist_right = A(row, col+1);
        tentative_dist(row, col+1) = min([tentative_dist(row, col+1), dist_right + current_dist]);
    catch
        dist_right = inf;
    end
    
    try
        dist_down = A(row+1, col);
        tentative_dist(row+1, col) = min([tentative_dist(row+1, col), dist_down + current_dist]);
    catch
        dist_down = inf;
    end
    
    unvisited_set(row, col) = NaN;
    
    if (row == target_row) & (col == target_col)
        break
    end
    
    tent_unvisited = tentative_dist .* unvisited_set;
    [min_val, indx] = min(tent_unvisited(:));
    
    [row, col] = ind2sub(size(A), indx);  
    
end

final_sum = A(1, 1) + tentative_dist(target_row, target_col);
fprintf(1, 'Final Sum: %i \n', final_sum)





