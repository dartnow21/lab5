from lab5.barriers import *
from lab5.Newton import *
from lab5.primal_dual import *
from lab5.handlers.input_validation import check_expression, check_restr, check_point
from lab5.handlers.prepocessing import prepare_all


class User:
    def userAnswer(self):
        """
        Функция создана дл упрощения работы пользователя с данной программой, тут представлены подсказки и премеры ввода
        данных.
        Returns
        ===========
        Обращается к нужной функции метода и передает ей необходимые параметры.
        """
        print(
            "Каким методом хотите воспользоваться?\n"
            "1 - Метод Ньютона \n"
            "2 - Прямой метод внутренней точки\n"
            "3 - Прямо-двойственным методом внутренней точки\n")

        user_answer = int(input())

        # Метод Ньютона
        if user_answer == 1:
            print("Введите функцию. Например x1**2 + x2**2 + (0.5*1*x1 + 0.5*2*x2)**2 + (0.5*1*x1 + 0.5*2*x2)**4")
            f = str(input())
            f_graph = copy.deepcopy(f)
            print(
                "Введите ограничение (если их несколько то ввести через точку с запятой как в примере). Например x1+x2=0;2*x1-3*x2=0")
            subject_to = str(input())
            # point_min = np.array([0, 0])
            # point_start = np.array([-5, 4.])
            print("Введите координаты начальной точки. Например -5;4")
            point_start = str(input())

            # input_validation
            f = check_expression(f)
            subject_to = check_restr(subject_to, method='Newton')
            point_start = check_point(point_start, f, subject_to, 'Newton')
            # preprocessing
            f, subject_to, point_start = prepare_all(f, subject_to, 'Newton', point_start)
            # solver
            task = Newton(f, subject_to, point_start)
            ans = task.solve()
            # print(np.allclose(ans, point_min))
            print(ans)

            # Рисуем график
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.set_title('Метод Ньютона')
            ax.set_zlabel('F(x1,x2)')
            ax.set_ylabel('x2')
            ax.set_xlabel('x1')

            x1 = np.linspace(-1, 1, 25)
            x2 = np.linspace(-1, 1, 25)
            x1, x2 = np.meshgrid(x1, x2)
            Z = ne.evaluate(f_graph)

            surf = ax.plot_surface(x1, x2, Z, cmap='viridis', shade=True, alpha=0.5)
            fig.colorbar(surf, shrink=0.5, aspect=10)

            func1 = sp.sympify(f_graph)

            x1, x2 = sp.symbols('x1 x2')

            ax.scatter(float(ans[0]), float(ans[1]),
                       func1.subs([(x1, float(ans[0])), (x2, float(ans[1]))]),
                       c='r', s=50,
                       label=f'Точка экстремума \n x1 = {float(ans[0])},\n x2 = {float(ans[1])},\n'
                             f' F(x1,x2) = {func1.subs([(x1, float(ans[0])), (x2, float(ans[1]))])}')

            ax.legend(labelcolor='black')
            plt.show()


        # Прямой метод внутренней точки
        elif user_answer == 2:
            print("Введите функцию. Например x1**2 + x2**2 + (0.5*1*x1 + 0.5*2*x2)**2 + (0.5*1*x1 + 0.5*2*x2)**4")
            f = str(input())
            f_graph = copy.deepcopy(f)
            print(
                "Введите ограничение (если их несколько то ввести через точку с запятой как в примере). Например x1+x2=0;2*x1-3*x2=0")
            subject_to = str(input())
            # point_min = np.array([0, 0])
            # point_start = np.array([-5, 4.])
            print("Введите координаты начальной точки. Например -5;4")
            point_start = str(input())

            # input_validation
            f = check_expression(f)
            subject_to = check_restr(subject_to, method='log_barrier')
            point_start = check_point(point_start, f, subject_to, 'log_barrier')
            # preprocessing
            f, subject_to, point_start = prepare_all(f, subject_to, 'log_barrier', point_start)
            # solver
            task = LogBarrirers(f, subject_to, point_start)
            ans = task.solve()
            # print(np.allclose(ans, point_min))
            print(ans)

            # Рисуем график
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.set_title('Метод логарифмических барьеров ')
            ax.set_zlabel('F(x1,x2)')
            ax.set_ylabel('x2')
            ax.set_xlabel('x1')

            x1 = np.linspace(-1, 1, 25)
            x2 = np.linspace(-1, 1, 25)
            x1, x2 = np.meshgrid(x1, x2)
            Z = ne.evaluate(f_graph)

            surf = ax.plot_surface(x1, x2, Z, cmap='viridis', shade=True, alpha=0.5)
            fig.colorbar(surf, shrink=0.5, aspect=10)

            func1 = sp.sympify(f_graph)

            x1, x2 = sp.symbols('x1 x2')

            ax.scatter(float(ans[0]), float(ans[1]),
                       func1.subs([(x1, float(ans[0])), (x2, float(ans[1]))]),
                       c='r', s=50,
                       label=f'Точка экстремума \n x1 = {float(ans[0])},\n x2 = {float(ans[1])},\n'
                             f' F(x1,x2) = {func1.subs([(x1, float(ans[0])), (x2, float(ans[1]))])}')

            ax.legend(labelcolor='black')
            plt.show()

        # Прямо-двойственным методом внутренней точки
        elif user_answer == 3:
            print("Введите функцию. Например x1**2 + x2**2 + (0.5*1*x1 + 0.5*2*x2)**2 + (0.5*1*x1 + 0.5*2*x2)**4")
            f = str(input())
            f_graph = copy.deepcopy(f)
            print(
                "Введите ограничение (если их несколько то ввести через точку с запятой как в примере). Например x1+x2=0;2*x1-3*x2=0")
            subject_to = str(input())
            # point_min = np.array([0, 0])
            # point_start = np.array([-5, 4.])
            print("Введите координаты начальной точки. Например -5;4")
            point_start = str(input())

            # input_validation
            f = check_expression(f)
            subject_to = check_restr(subject_to, method='primal-dual')
            point_start = check_point(point_start, f, subject_to, 'primal-dual')
            # preprocessing
            f, subject_to, point_start = prepare_all(f, subject_to, 'primal-dual', point_start)
            # solver
            task = PrimalDual(f, subject_to, point_start)
            ans = task.solve()
            print(ans[0])

            # Рисуем график
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.set_title('Прямо-двойственный метод внутренней точки')
            ax.set_zlabel('F(x1,x2)')
            ax.set_ylabel('x2')
            ax.set_xlabel('x1')

            x1 = np.linspace(-1, 1, 25)
            x2 = np.linspace(-1, 1, 25)
            x1, x2 = np.meshgrid(x1, x2)
            Z = ne.evaluate(f_graph)

            surf = ax.plot_surface(x1, x2, Z, cmap='viridis', shade=True, alpha=0.5)
            fig.colorbar(surf, shrink=0.5, aspect=10)

            func1 = sp.sympify(f_graph)

            x1, x2 = sp.symbols('x1 x2')

            ax.scatter(float(ans[0][0]), float(ans[0][1]),
                       func1.subs([(x1, float(ans[0][0])), (x2, float(ans[0][1]))]),
                       c='r', s=50,
                       label=f'Точка экстремума \n x1 = {float(ans[0][0])},\n x2 = {float(ans[0][1])},\n'
                             f' F(x1,x2) = {func1.subs([(x1, float(ans[0][0])), (x2, float(ans[0][1]))])}')

            ax.legend(labelcolor='black')
            plt.show()

        else:
            print('Введен неверный номер')


functionss = User()
functionss.userAnswer()
