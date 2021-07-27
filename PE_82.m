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
start_rows = 1:size(A, 1);
sum_vec = [];

% Try each possible start row
for row_ind = start_rows

    unvisited_set = ones(size(A));
    tentative_dist = inf(size(A));
    tentative_dist(row_ind, 1) = 0;
    current_node = zeros(size(A));
    current_node(row_ind, 1) = 1;

    target_col = size(A, 2);  % we just want to end up in the right most column

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

        tent_unvisited = tentative_dist .* unvisited_set;
        [min_val, indx] = min(tent_unvisited(:));
        
        row_prev = row;
        col_prev = col;
        [row, col] = ind2sub(size(A), indx);  
        
        if (row_prev == row) & (col_prev == col)
            break
        end
        
    end
    
    final_sum = A(row_ind, 1) + tentative_dist;
    sum_vec = [sum_vec, final_sum(:, target_col)];
        

end

disp(sum_vec)
disp(min(sum_vec(:)))

% Answer: 260324 - very good! 







