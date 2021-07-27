clear all
close all

file_path = 'p082_matrix.txt';  % Same as problem 81 matrix I believe

% Sample Matrix
% A = [[131, 673, 234, 103, 18];
%     [201, 96, 342, 965, 150];
%     [630, 803, 746, 422, 111];
%     [537, 699, 497, 121, 956];
%     [805, 732, 524, 37, 331]];

A = readmatrix(file_path);

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
    try  % Right
        dist_right = A(row, col+1);
        tentative_dist(row, col+1) = min([tentative_dist(row, col+1), dist_right + current_dist]);
    catch
        dist_right = inf;
    end
    
    try  % Left
        dist_left = A(row, col-1);
        tentative_dist(row, col-1) = min([tentative_dist(row, col-1), dist_left + current_dist]);
    catch
        dist_left = inf;
    end
    
    try  % Down
        dist_down = A(row+1, col);
        tentative_dist(row+1, col) = min([tentative_dist(row+1, col), dist_down + current_dist]);
    catch
        dist_down = inf;
    end
    
    try  % Up
        dist_up = A(row-1, col);
        tentative_dist(row-1, col) = min([tentative_dist(row-1, col), dist_up + current_dist]);
    catch
        dist_up = inf;
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

% Answer - Final Sum: 425185  - very good! 
% Note I was concerned about looping and needing to overwrite the visited
% indices, but I see now that was not a major concern (i.e. we cannot form
% a loop when minimzing, we would simply cut out the loop







